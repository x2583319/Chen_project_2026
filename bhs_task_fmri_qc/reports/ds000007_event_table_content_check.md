# ds000007 Event-table Content Check

## File checked

- ds000007_first_events.tsv

## Basic summary

- Rows: 128
- Columns: onset, duration, trial_type, TrialType, model, cond, Stimulus, SSD, Response, ReactionTime, CorrectGo, SuccStop
- Required BIDS timing columns present: PASS

## Detected columns

- onset: present
- duration: present
- trial_type: present
- TrialType: present
- model: present
- cond: present
- Stimulus: present
- SSD: present
- Response: present
- ReactionTime: present
- CorrectGo: present
- SuccStop: present

## Example rows

|   onset |   duration | trial_type      |   TrialType | model    | cond    |   Stimulus |   SSD |   Response |   ReactionTime |   CorrectGo |   SuccStop |
|--------:|-----------:|:----------------|------------:|:---------|:--------|-----------:|------:|-----------:|---------------:|------------:|-----------:|
|    0    |        1.5 | successful stop |           1 | model001 | cond002 |          1 | 0.113 |          0 |          0     |           0 |          1 |
|    3.25 |        1.5 | go              |           0 | model001 | cond001 |          0 | 0     |         49 |          0.389 |           1 |          0 |
|    7.25 |        1.5 | go              |           0 | model001 | cond001 |          0 | 0     |         49 |          0.429 |           1 |          0 |
|    9.63 |        1.5 | go              |           0 | model001 | cond001 |          1 | 0     |         50 |          0.413 |           1 |          0 |
|   12.13 |        1.5 | go              |           0 | model001 | cond001 |          0 | 0     |         49 |          0.361 |           1 |          0 |