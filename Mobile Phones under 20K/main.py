import requests
from bs4 import BeautifulSoup
import pandas as pd

item_list = []

for page_num in range(1,16):
    url = f"https://www.flipkart.com/search?q=mobiles+under+20000&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page={page_num}"

    header = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36 Edg/131.0.0.0', 'Accept-Language': 'en-US,en;q=0.5', 'Connection': 'keep-alive' }

    response = requests.get(url, headers=header)

    soup = BeautifulSoup(response.content, "html.parser")


    items_referal = soup.find_all('a',class_='CGtC98')
    for item in items_referal:
        item_list.append(f"https://flipkart.com{item.get('href')}")

final_list = []

column_headers = [
    "Mobile Link",
    "Mobile Name",
    "Price",
    "Rating",
    "SIM Type",
    "Display Size",
    "Resolution",
    "Display Type",
    "GPU",
    "Operating System",
    "Processor Type",
    "Processor Core",
    "Internal Storage",
    "RAM",
    "Total Memory",
    "Expandable Storage",
    "Primary Camera",
    "Secondary Camera",
    "Digital Zoom",
    "Frame Rate",
    "Supported Networks",
    "Bluetooth Version",
    "Wi-Fi Version",
    "NFC",
    "Battery Capacity"
]

def safe_extract_text(element, default="N/A"):
    return element.text.strip() if element else default

for referals in item_list:
    url = referals
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.content, 'html.parser')

    titles = soup.findAll('td', attrs={'class': "+fFi1w"})
    title_list = []

    content = soup.findAll('li', attrs={'class': 'HPETK2'})
    content_list = []

    price = soup.find('div', attrs={'class':'Nx9bqj CxhGGd'})
    mobile = soup.find('span',attrs={'class':'VU-ZEz'})
    rating = soup.find('div', attrs={'class':'ipqd2A'})

    # Collect titles and content
    for i in titles:
        title_list.append(i.text)

    for j in content:
        content_list.append(j.text)

    
    new_list = [
        url,
        safe_extract_text(mobile),
        safe_extract_text(price),
        safe_extract_text(rating),
    ]

    
    # Define a helper function to get the index safely
    def get_index_safe(title, title_list):
        try:
            return title_list.index(title)
        except ValueError:
            return None 

    # Extract indices
    sim_type = get_index_safe("SIM Type", title_list)
    display_size = get_index_safe("Display Size", title_list)
    resolution = get_index_safe("Resolution", title_list)
    display_type = get_index_safe("Display Type", title_list)
    gpu = get_index_safe("GPU", title_list)
    operating_system = get_index_safe("Operating System", title_list)
    processor_type = get_index_safe("Processor Type", title_list)
    processor_core = get_index_safe("Processor Core", title_list)
    internal_storage = get_index_safe("Internal Storage", title_list)
    ram = get_index_safe("RAM", title_list)
    total_mem = get_index_safe("Total Memory", title_list)
    expandable = get_index_safe("Expandable Storage", title_list)
    prime_camera = get_index_safe("Primary Camera", title_list)
    secondary_camera = get_index_safe("Secondary Camera", title_list)
    digital_zoom = get_index_safe("Digital Zoom", title_list)
    frame_rate = get_index_safe("Frame Rate", title_list)
    supported_net = get_index_safe("Supported Networks", title_list)
    bluetooth_v = get_index_safe("Bluetooth Version", title_list)
    wifi_v = get_index_safe("Wi-Fi Version", title_list)
    nfc = get_index_safe("NFC", title_list)
    battery = get_index_safe("Battery Capacity", title_list)

    
    if sim_type is not None:
        new_list.append(content_list[sim_type])
    else:
        new_list.append("N/A")

    if display_size is not None:
        new_list.append(content_list[display_size])
    else:
        new_list.append("N/A")

    if resolution is not None:
        new_list.append(content_list[resolution])
    else:
        new_list.append("N/A")

    if display_type is not None:
        new_list.append(content_list[display_type])
    else:
        new_list.append("N/A")

    if gpu is not None:
        new_list.append(content_list[gpu])
    else:
        new_list.append("N/A")

    if operating_system is not None:
        new_list.append(content_list[operating_system])
    else:
        new_list.append("N/A")

    if processor_type is not None:
        new_list.append(content_list[processor_type])
    else:
        new_list.append("N/A")

    if processor_core is not None:
        new_list.append(content_list[processor_core])
    else:
        new_list.append("N/A")

    if internal_storage is not None:
        new_list.append(content_list[internal_storage])
    else:
        new_list.append("N/A")

    if ram is not None:
        new_list.append(content_list[ram])
    else:
        new_list.append("N/A")

    if total_mem is not None:
        new_list.append(content_list[total_mem])
    else:
        new_list.append("N/A")

    if expandable is not None:
        new_list.append(content_list[expandable])
    else:
        new_list.append("N/A")

    if prime_camera is not None:
        new_list.append(content_list[prime_camera])
    else:
        new_list.append("N/A")

    if secondary_camera is not None:
        new_list.append(content_list[secondary_camera])
    else:
        new_list.append("N/A")

    if digital_zoom is not None:
        new_list.append(content_list[digital_zoom])
    else:
        new_list.append("N/A")

    if frame_rate is not None:
        new_list.append(content_list[frame_rate])
    else:
        new_list.append("N/A")

    if supported_net is not None:
        new_list.append(content_list[supported_net])
    else:
        new_list.append("N/A")

    if bluetooth_v is not None:
        new_list.append(content_list[bluetooth_v])
    else:
        new_list.append("N/A")

    if wifi_v is not None:
        new_list.append(content_list[wifi_v])
    else:
        new_list.append("N/A")

    if nfc is not None:
        new_list.append(content_list[nfc])
    else:
        new_list.append("N/A")

    if battery is not None:
        new_list.append(content_list[battery])
    else:
        new_list.append("N/A")

    final_list.append(new_list)


df = pd.DataFrame(final_list,columns=column_headers)
df.to_csv("Mobiles under 20,000.csv")
print("File Saved")
