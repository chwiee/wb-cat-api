import requests
import json
import mysql.connector as conn

header = {'Content-Type': 'application/json',
          'x-api-key': "3571fdbb-fe12-40aa-b190-b142ee22a961"
        }

# returns all data of the 67 Breed registered in the API, also returns 3 url of images of each Breed
def get_breeds(u, h):
  #Create lists:
  val = {}
  img = {} 
  #Print init
  print('Populate a CAT table...')
  #Get cat data:
  response = requests.get(u, h)
  #Load json:
  data = json.loads(response.text)
  #Loop to populate values whith cat data:
  for i in range (1, 67):
    val[0] = data[i]['id']
    val[1] = data[i]['name']
    val[2] = data[i]['origin']
    val[3] = data[i]['temperament']
    val[4] = data[i]['description'][:40]
    #Get cat images with breed_id selector:
    response2 = requests.get('https://api.thecatapi.com/v1/images/search?breed_id=' + data[i]['id'] + '&limit=3', h)  
    #Load json:
    data2 = json.loads(response2.text)
    #Ignore Out Index Error in Python:
    try:
      #Loop to populate list with cat images (3):
      for j in range (0, 3):
        img[j] = data2[j]['url']
    except:
      pass
    #Check URL:
    if len(img) == 3:
      pass
    elif len(img) == 2:
      img[2]="Null"
    else:
      img[1]="Null"
      img[2]="Null"
    #Create MySQL Con:
    con_mysql = conn.connect(
      host="localhost",
      port=3306,
      user="devops",
      passwd="mestre",
      db="cat"
    )
    #Create MySQL Cursor:
    cursor = con_mysql.cursor()
    #Execute insert:
    cursor.execute("INSERT INTO cats (id_api, name, origin, temperament, description, img_url1, img_url2, img_url3) VALUES ('" + val[0] + "', '" + val[1] + "', '" + val[2] + "', '" + val[3] + "', '" + val[4] + "', '" + img[0] + "', '" + img[1] + "', '" + img[2] + "');")
    #Commit execution:
    con_mysql.commit()
    #Close Cursor:
    cursor.close()
    #Close Con:
    con_mysql.close()
    #Print new entry
    print(' New entry ' + val[1] + ' add in "CAT" table')
    #Clear lists:
    val.clear()
    img.clear()

# returns 3 url of images if i = 0 Cats with hats | i = 1 cats with glasses
def get_cat_category(u, h):
  #Create list
  val = {}
  img = {}
  #Get cat data
  response = requests.get(u, h)
  #Load json
  data = json.loads(response.text)
  #Get categories name
  val[0] = data[0]['categories'][0]['name']
  #Loop to get 3 images with categorie selector
  for i in range (0, 3):
    img[i] = data[i]['url']
  #Create MySQL Con
  con_mysql = conn.connect(
    host="localhost",
    port=3306,
    user="devops",
    passwd="mestre",
    db="cat"
  )
  #Create MySQL Cursor
  cursor = con_mysql.cursor()
  #Execute Insert
  cursor.execute("INSERT INTO cats (id_api, img_url1, img_url2, img_url3) VALUES ('" + val[0] + "', '" + img[0] + "', '" + img[1] + "', '" + img[2] + "')")
  #Commit execution
  con_mysql.commit() 
  #Close Cursor
  cursor.close()
  #Close Con
  con_mysql.close()
  print(' New entry from "CAT" table: ' + val[0] + ' add 3 images')



get_breeds('https://api.thecatapi.com/v1/breeds', header)

for i in range(0, 2):
  if i == 0:
    #Hats
    get_cat_category('https://api.thecatapi.com/v1/images/search?limit=3&category_ids=1', header)
  else:
    #SunGlasses
    get_cat_category('https://api.thecatapi.com/v1/images/search?limit=3&category_ids=4', header)
