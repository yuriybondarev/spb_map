import pandas as pd

# f1 = open('spb_posts_2019.csv','r', encoding='utf-8')
df1 = pd.read_csv("spb_posts_2019.csv", sep=",")
print(set(df1['isad']))
# id,shortcode,imageurl,isvideo,caption,commentscount,timestamp,likescount,isad,authorid,locationid,lat,lon
# print(set(df1['caption'][0]))
# df2 = df1.query("isad != 'f'")
# df2.to_csv("spb_posts_2019_ads.csv")
input()