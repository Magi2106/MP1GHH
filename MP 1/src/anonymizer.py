import hashlib

def anonymize(df, column):
    df[column] = df[column].apply(lambda x: hashlib.sha256(str(x).encode()).hexdigest())
    return df