#!/usr/bin/env python

import stats

test_cases = [('chicago', 'march', 'friday'), ('chicago', 'june', 'all'),
              ('washington', 'january', 'friday'),
              ('washington', 'all', 'all')]

for item in test_cases:
    city, month, day = item
    df = stats.load_data(city, month, day)

    print(df.head(3))
    stats.time_stats(df)
    stats.station_stats(df)
    stats.trip_duration_stats(df)
    stats.user_stats(df)
