import pkg_resources


print(pkg_resources.get_distribution("datetime").version)
print(pkg_resources.get_distribution("vk_api").version)
print(pkg_resources.get_distribution("pytelegrambotapi").version)
