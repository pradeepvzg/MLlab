group1 = [23, 45, 67, 34, 45]
group2 = [56, 78, 76, 87, 89]
group3 = [65, 75, 85, 55, 65]

all_data = group1 + group2 + group3

grand_mean = sum(all_data) / len(all_data)

mean1 = sum(group1) / len(group1)
mean2 = sum(group2) / len(group2)
mean3 = sum(group3) / len(group3)

ssb = len(group1) * (mean1 - grand_mean) ** 2 + len(group2) * (mean2 - grand_mean) ** 2 + len(group3) * (mean3 - grand_mean) ** 2

ssw = sum((x - mean1) ** 2 for x in group1) + sum((x - mean2) ** 2 for x in group2) + sum((x - mean3) ** 2 for x in group3)

df_between = 3 - 1
df_within = len(all_data) - 3

msb = ssb / df_between
msw = ssw / df_within


f_stat = msb / msw

print(f'F-statistic: {f_stat}')
