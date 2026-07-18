import pandas as pd


class DataEngine:

    def __init__(self, csv_file):

        self.csv_file = csv_file
        self.df = None

        # Cache prepared feature vectors
        self.feature_cache = {}

    # =====================================================
    # Load Dataset
    # =====================================================

    def load_data(self):

        print("Loading dataset...")

        self.df = pd.read_csv(self.csv_file)

        print("Dataset Loaded Successfully")
        print(f"Rows    : {len(self.df)}")
        print(f"Columns : {len(self.df.columns)}")

    # =====================================================
    # Process Date
    # =====================================================

    def process_dates(self):

        print("Processing dates...")

        self.df["DATE"] = pd.to_datetime(
            self.df["DATE"].astype(str),
            format="%Y%m%d"
        )

        self.df["Year"] = self.df["DATE"].dt.year
        self.df["Month"] = self.df["DATE"].dt.month
        self.df["Day"] = self.df["DATE"].dt.day

        print("Date Processing Completed")

    # =====================================================
    # Feature Engineering
    # =====================================================

    def create_features(self):

        print("Creating AI Features...")

        # Keep same preprocessing used while training
        self.df = self.df.sort_values("DATE")

        # Lag Features
        self.df["malaria_cases_lag_1"] = self.df["malaria_cases"].shift(1)
        self.df["malaria_cases_lag_7"] = self.df["malaria_cases"].shift(7)
        self.df["malaria_cases_lag_14"] = self.df["malaria_cases"].shift(14)

        # Rolling Features
        self.df["T2M_roll7"] = self.df["T2M"].rolling(window=7).mean()
        self.df["RH2M_roll7"] = self.df["RH2M"].rolling(window=7).mean()
        self.df["PRECIP_roll7"] = self.df["PRECIP"].rolling(window=7).mean()

        # Remove incomplete rows
        self.df = self.df.dropna().reset_index(drop=True)

        print("Feature Engineering Completed")

    # =====================================================
    # Initialize Once
    # =====================================================

    def initialize(self):

        # Already initialized
        if self.df is not None:
            return

        self.load_data()
        self.process_dates()
        self.create_features()

        print("\n✅ Data Engine Ready")

    # =====================================================
    # District List
    # =====================================================

    def get_districts(self):

        return sorted(self.df["District"].unique())

    # =====================================================
    # Latest Record
    # =====================================================

    def get_latest_record(self, district):

        district_df = self.df[self.df["District"] == district]

        if district_df.empty:
            return None

        return district_df.iloc[-1]

    # =====================================================
    # Prepare Features
    # =====================================================

    def prepare_features(self, district):

        # Return cached version if available
        if district in self.feature_cache:
            return self.feature_cache[district]

        row = self.get_latest_record(district)

        if row is None:
            return None

        features = pd.DataFrame([{

            "T2M": row["T2M"],
            "RH2M": row["RH2M"],
            "PRECIP": row["PRECIP"],
            "Latitude": row["Latitude"],
            "Longitude": row["Longitude"],
            "malaria_deaths": row["malaria_deaths"],

            "malaria_cases_lag_1": row["malaria_cases_lag_1"],
            "malaria_cases_lag_7": row["malaria_cases_lag_7"],
            "malaria_cases_lag_14": row["malaria_cases_lag_14"],

            "T2M_roll7": row["T2M_roll7"],
            "RH2M_roll7": row["RH2M_roll7"],
            "PRECIP_roll7": row["PRECIP_roll7"],

            "Year": row["Year"],
            "Month": row["Month"],
            "Day": row["Day"]

        }])

        # Store in cache
        self.feature_cache[district] = features

        return features

    # =====================================================
    # Get Complete Record
    # =====================================================

    def get_record(self, district):

        row = self.get_latest_record(district)

        if row is None:
            return None

        return row.to_dict()

    # =====================================================
    # Clear Cache (Optional)
    # =====================================================

    def clear_cache(self):

        self.feature_cache.clear()

        print("Feature cache cleared.")