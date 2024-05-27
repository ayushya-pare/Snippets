import pandas as pd
import matplotlib.pyplot as plt

# Sample Series for demonstration
series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Plotting
series.plot(title='Line Plot')
plt.show()

series.hist(title='Histogram')
plt.show()

series.plot.box(title='Box Plot')
plt.show()

series.plot.kde(title='Density Plot')
plt.show()

series.plot.bar(title='Bar Plot')
plt.show()

# Statistical Analysis
summary_stats = series.describe()
print("Summary Statistics:\n", summary_stats)

value_counts = series.value_counts()
print("Value Counts:\n", value_counts)

mean = series.mean()
median = series.median()
mode = series.mode()
print(f"Mean: {mean}, Median: {median}, Mode: {mode}")

variance = series.var()
std_dev = series.std()
print(f"Variance: {variance}, Standard Deviation: {std_dev}")

# Assuming other_series is another pd.Series object
other_series = pd.Series([2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
correlation = series.corr(other_series)
covariance = series.cov(other_series)
print(f"Correlation: {correlation}, Covariance: {covariance}")

# Merging and Concatenation
series1 = pd.Series([1, 2, 3])
series2 = pd.Series([4, 5, 6])
combined_series = pd.concat([series1, series2])
print("Combined Series:\n", combined_series)

appended_series = series1.append(series2)
print("Appended Series:\n", appended_series)

df = pd.DataFrame({'A': [1, 2, 3]})
merged_df = pd.merge(df, series1.to_frame(name='B'), left_index=True, right_index=True)
print("Merged DataFrame:\n", merged_df)

# Transformations
transformed_series = series.apply(lambda x: x**2)
print("Transformed Series (squared values):\n", transformed_series)

mapped_series = series.map({1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: 'I', 10: 'J'})
print("Mapped Series:\n", mapped_series)

sorted_series = series.sort_values()
print("Sorted Series:\n", sorted_series)

threshold_value = 5
filtered_series = series[series > threshold_value]
print("Filtered Series (values > threshold):\n", filtered_series)

# Handling Missing Data
series_with_nan = pd.Series([1, 2, None, 4, None, 6])
filled_series = series_with_nan.fillna(0)
print("Filled Series (NaN filled with 0):\n", filled_series)

dropped_series = series_with_nan.dropna()
print("Dropped Series (NaN values dropped):\n", dropped_series)

# Time Series Analysis (if applicable)
time_series = pd.Series([1, 2, 3, 4, 5, 6], 
                        index=pd.date_range('2020-01-01', periods=6, freq='D'))
resampled_series = time_series.resample('M').mean()
print("Resampled Series (Monthly mean):\n", resampled_series)

rolling_series = time_series.rolling(window=3).mean()
print("Rolling Window Series (window=3):\n", rolling_series)

differenced_series = time_series.diff()
print("Differenced Series:\n", differenced_series)
