import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    
    # Sort by id so smallest id comes first
    person.sort_values(by="id", inplace=True)
    
    # Remove duplicate emails and keep first occurrence
    person.drop_duplicates(
        subset="email",
        keep="first",
        inplace=True
    )