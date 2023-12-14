import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Read JSON into DataFrame
df_list = []
with open('src/yelp_academic_dataset_review.json', encoding='utf-8') as f:
    df_reader = pd.read_json(f, lines=True, chunksize=100)
    for chunk in df_reader:
        df_list.append(chunk)

# Concatenate the list of DataFrames into a single DataFrame
df = pd.concat(df_list, ignore_index=True)

# star1_comments = data[data['stars'] == 1.0]['text'].iloc[:array_split].tolist()
# star2_comments = data[data['stars'] == 2.0]['text'].iloc[:array_split].tolist()
# star3_comments = data[data['stars'] == 3.0]['text'].iloc[:array_split].tolist()
# star4_comments = data[data['stars'] == 4.0]['text'].iloc[:array_split].tolist()
# star5_comments = data[data['stars'] == 5.0]['text'].iloc[:array_split].tolist()


# df_star1 = pd.DataFrame({'text': star1_comments, 'stars': 1})
# df_star2 = pd.DataFrame({'text': star2_comments, 'stars': 2})
# df_star3 = pd.DataFrame({'text': star3_comments, 'stars': 3})
# df_star4 = pd.DataFrame({'text': star4_comments, 'stars': 4})
# df_star5 = pd.DataFrame({'text': star5_comments, 'stars': 5})

# Convert DataFrame to Arrow Table
table = pa.Table.from_pandas(df)

# Write Arrow Table to Parquet file
pq.write_table(table, 'output.parquet')
