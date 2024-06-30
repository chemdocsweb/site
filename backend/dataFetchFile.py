def textbooksData(link):
  import requests as rq
  import pandas as pd
  from io import StringIO
  
  response = rq.get(link)
  response.raise_for_status()

  csv_data = StringIO(response.text)
  textbooks = pd.read_csv(csv_data)
  
  subjects_info = textbooks[['subject', 'sub_info']].drop_duplicates()
  subs_count = list(range(1, len(subjects_info['subject']) + 1))
  
  subjects_info = subjects_info.to_dict("records")
  textbooks = textbooks.to_dict("records")
  
  return subs_count, subjects_info, textbooks