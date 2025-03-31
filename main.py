from selenium import webdriver
from selenium.webdriver.common.by import By



def get_more_details(path):
    data = {"Topics": None, "Articles": None, "Types": None,"Descriptions": None}

    local_driver = webdriver.Chrome()
    local_driver.get(path)

    topic_driver = local_driver.find_element(By.XPATH, '//ul[@class="CourseModulesList_modulesList__C86yL"]')
    topics = topic_driver.find_elements(By.XPATH, './/li[@class="color-dark-blue"]')

    description = local_driver.find_element(By.XPATH, '//p[@class="typography_textMain__oRJ69 SalarySection_aboutProfession__C6ftM"]').get_attribute('innerText')

    learn_types = local_driver.find_elements(By.XPATH, '//p[@class = "LandingTables_columnHeaderWhite__577Bn align-center"]')
    learn_type = set(x.get_attribute('innerText') for x in learn_types)
    data['Types'] = ["Flex", "Offline"] if len(learn_type) == 2 else ["Flex"] if learn_type.__contains__("У вільний час") else ["Offline"]
    data['Topics'] = len(topics)
    data["Articles"] = sum(int(topic.find_element(By.XPATH, './/p[@class="CourseModulesList_topicsCount__H_fv3 typography_textMain__oRJ69"]').get_attribute('innerHTML').split()[0]) for topic in topics)
    data['Descriptions'] = description
    local_driver.quit()

    return data
def show_result(result):
    for key, value in result.items():
        print(f"{key}: {value}\n")

def main():
    driver = webdriver.Chrome()
    driver.get("https://mate.academy")

    result = {}
    link_driver = driver.find_element(By.XPATH, '//ul[@class = "DropdownProfessionsList_list__8OXQk"]')

    links = link_driver.find_elements(By.TAG_NAME, 'a')
    courses = link_driver.find_elements(By.TAG_NAME, 'span')

    course_names = [x.get_attribute('innerHTML') for x in courses]
    clear_links = [link.get_attribute('href') for link in links[::2]]
    print(clear_links)
    for i in range(0, len(clear_links)):
        result[f"{course_names[i]}"] = get_more_details(clear_links[i])
    driver.quit()
    show_result(result)

if __name__ == '__main__':
    main()