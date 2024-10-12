photos = []

unique_names = {}
max_photos = None

def count_peoples(photos: dict):
    for item in photos:
        photo_id = item['id']
        for name in item['names']: 
            if name not in unique_names:
                unique_names[name] = [photo_id]
            else:
                unique_names[name].append(photo_id)
                
    # filtrar pessoas maiores aparições
    people_more_often = [name if len(unique_names[name]) == max([len(unique_names[name]) for name in unique_names]) else None for name in unique_names]
    people_more_often = sorted(list(filter(None, people_more_often)))[0]

    photos_often = " ".join(str(item) for item in unique_names[people_more_often])

    print(f"No total, {len(unique_names)} pessoas apareceram nas fotos.")
    print(f"{people_more_often} foi a pessoa mais frequente, aparecendo na(s) foto(s): {photos_often}")
    return

while True:
    if max_photos == None:
        n = input()
        max_photos = int(n)

    (photo_id, names) = input().split(':')
    photo_id = int(photo_id.split(' ')[1])

    if names != '':
        photos.append({
            "id": photo_id,
            "names": names.lstrip().split(', ')
        })

    if photo_id == max_photos:
        count_peoples(photos)
        break