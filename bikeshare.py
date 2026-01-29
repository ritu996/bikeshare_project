VALID_CITIES = ['chicago', 'new york city', 'washington']
VALID_MONTHS = ['january', 'february', 'march', 'april', 'may', 'june', 'all']
VALID_DAYS = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']
def get_filters() -> tuple[str, str, str]:
    city = 'chicago'
    month = 'all'
    day = 'all'
    return city, month, day
def most_common_stat(df: pd.DataFrame, column: str) -> str:
    if column in df:
        return df[column].mode()[0]
    return "N/A"

