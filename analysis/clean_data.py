def clean_data(data):
    for name, df in data.items():
        data[name] = df.dropna()
    return data

if __name__ == "__main__":
    from load_data import load_data
    
    data = load_data()
    clean_data = clean_data(data)
    for name, df in clean_data.items():
        print(f"{name} cleaned data preview:")
        print(df.head(), "\n")
