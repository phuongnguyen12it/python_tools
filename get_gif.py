from bs4 import BeautifulSoup
import requests

def get_home_page():
        try:
            body = requests.get('http://9gag.com/gif')
            if body.status_code == 200:
                html = BeautifulSoup(body.text, "html.parser")
                articles = html.find_all('article')
                return articles
        except:
            print("Fuck Error!")
        return False

def parse_data(origin_data):
	#Mang lua du lieu da xu ly
	list_parse_data = []

	for value in origin_data:
		#tao 1 obj de luu lai thong tin trich xuat
		obj_save={
			'name'	: '',
			'slug'	: '',
			'webm'	: '',
			'mp4'	: '',
			'image'	: '',
		}
		html = BeautifulSoup(str(value), "html.parser")
		try:
			obj_save['name']	= html.find('h2', {'class': 'badge-item-title'}).text.strip()
			obj_save['image']	= html.find('img', {'class': 'badge-item-img'}).attrs['src'].strip()

			sources	= html.find_all('source')
			for source in sources:
				src = source.attrs['src']
				if ('mp4' in src):
					obj_save['mp4'] = src
				elif ('webm' in src):
					obj_save['webm']= src

			list_parse_data.append(source)
		except:
			print('Some pare data error')
		return list_parse_data

print("-------------------------GET-HOME_PAGE-------------------------------------")
print("\t ", get_home_page())
print("-------------------------END GET-HOME_PAGE-------------------------------------")


print("-------------------------parse_data-------------------------------------")
print("\t ", parse_data(get_home_page()))
print("-------------------------end parse_data-------------------------------------")
