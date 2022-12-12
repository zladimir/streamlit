import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd


def create_icon(url: str) -> folium.features.CustomIcon:
    return folium.features.CustomIcon(url, icon_size=(80, 80))


def create_places() -> pd.DataFrame:
    places = pd.DataFrame(columns=['longitude', 'latitude', 'url', 'description'])

    places = places.append(
        {
            'longitude': 55.766385,
            'latitude': 37.662201,
            'url': 'https://mymoscow.su/wp-content/uploads/2020/01/dom-shkatulochka-na-staroj-basmannoj-aa30c19.jpg',
            'head': 'Старинная купеческая усадьба',
            'year': '18 век',
            'arch': 'П.К. Микини',
            'style': '',
            'description': 'Комплекс включает в себя две постройки: главный усадебный дом, построенный в 18 веке по проекту неизвестного архитектора и перестроенный в 19-м по проекту Германа фон Ниссена, а также флигель, построенный в 1902 году по проекту архитектора Петра Микини. Главный дом уходит вглубь владения, располагаясь к улице торцом: его фасады, выполненные в жёлтом цвете, украшают пилястры и рустовка, а на крыше установлены декоративные вазоны.'
        },
        ignore_index=True
    )

    places = places.append(
        {
            'longitude': 55.767306,
            'latitude': 37.664644,
            'url': 'https://mahm.ru/img/gallery/7651e2135a504e39ebbd77528e0dc775.jpg',
            'head': 'Усадьба Муравьевых-Апостола',
            'year': '1803г',
            'arch': 'Кристофер Муравьев-Апостол',
            'style': 'Классицизм',
            'description': 'Дом-музей Матвея Муравьева-Апостола был открыт в 2013 году. Старинная городская усадьба была отреставрирована на средства Кристофера Муравьева-Апостола, гражданина Швейцарии, потомка семьи Муравьевых-Апостолов. В главном доме усадьбы был создан музей с небольшой постоянной экспозицией и с постоянно меняющимися выставками живописи и фотографии.'
        },
        ignore_index=True
    )

    places = places.append(
        {
            'longitude': 55.766739,
            'latitude': 37.663297,
            'url': 'https://avatars.mds.yandex.net/get-altay/1678797/2a0000016976cfe6a51121922b37d88fe970/XXL',
            'head': 'Городская усадьба Демидова П.И.-А.Б. Куракина ',
            'year': '18 век-19 век',
            'arch': 'Е.Д. Тюрин, Фрейденберг, Р.Р. Казаков',
            'style': 'Эклектика',
            'description': 'Величественное здание с массивным центральным ризалитом и двумя боковыми меньшего размера, окрашенное в два оттенка зелёного цвета.'
        },
        ignore_index=True
    )

    places = places.append(
        {
            'longitude': 55.768456,
            'latitude': 37.668058,
            'url': 'http://mosprogulka.ru/_pu/7/76138109.jpg',
            'head': 'Дом-музей художника Рокотова',
            'year': '1786-1803 год',
            'arch': 'Неизвестен',
            'style': 'Классицизм',
            'description': 'Дом Рокотова - сохранившийся двухэтажный флигель старинной городской усадьбы, существовавшей на углу Старой Басманной улицы'
        },
        ignore_index=True
    )

    places = places.append(
        {
            'longitude': 55.769059,
            'latitude': 37.668983,
            'url': 'https://a-a-ah-ru.s3.amazonaws.com/uploads/items/142773/292505/large_365a1416.jpg',
            'head': 'Дом-музей В.Л.Пушкина',
            'year': '1819 год',
            'arch': 'П.В.Кетчер',
            'style': 'Классицизм',
            'description': 'В обстановке старинного дома В.Л. Пушкина, в интерьерах XIX века, в кругу неизвестных, удивляющих своей красотой и историей бытования предметов посетители знакомятся с предметами эпохи, материалами, рассказывающими о Москве пушкинского детства, творчестве В.Л. Пушкина.'
        },
        ignore_index=True
    )


def main():
    st.set_page_config(layout='wide')
    st.title('Достопримечательности Москвы')
    m = folium.Map(location=[55.767306, 37.664644], zoom_start = 16)
    places = create_places()
    for _index, row in places.iterrows():
        lon = row["longitude"]
        lat = row["latitude"]
        icon = create_icon(row["url"])
        iframe = folium.IFrame(f'<h3> <b>{row["head"]} </h3> </b>' +\
                               f'<br><b>Год постройки:</b> {row["year"]}' +\
                               f'<br><b>Архитектор:</b> {row["arch"]}' +\
                               f'<br><b>Стиль:</b> {row["style"]}' +\
                               f'<br> {row["description"]}')
        popup = folium.Popup(iframe, min_width=400, max_width=400)
        marker = folium.map.Marker([lon, lat], icon=icon,
                                   popup=popup)
        marker.add_to(m)
    
    folium_static(m, width=1600, height=800)

if __name__ == '__main__':
    main()