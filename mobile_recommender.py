from tkinter import *
from functools import partial

class MobileRecommender:
	def __init__(self):
		self.company = ""
		self.ram = 0
		self.storage = 0
		self.filtered = []

		# Store smartphone data in a list
		self.specifications = [
		{"Model": "Samsung Galaxy M30s", "Company": "Samsung", "RAM": 4, "Storage": 64, "BCapacity": 6000, "Price": 13999, "OS": "Android"},
		{"Model": "Samsung Galaxy M51", "Company": "Samsung", "RAM": 6, "Storage": 128, "BCapacity": 7000, "Price": 22499, "OS": "Android"},
		{"Model": "Samsung Galaxy M31", "Company": "Samsung", "RAM": 6, "Storage": 64, "BCapacity": 6000, "Price": 15499, "OS": "Android"},
		{"Model": "Samsung Galaxy M11", "Company": "Samsung", "RAM": 3, "Storage": 32, "BCapacity": 5000, "Price": 9399, "OS": "Android"},
		{"Model": "Samsung Galaxy M10s", "Company": "Samsung", "RAM": 3, "Storage": 32, "BCapacity": 4000, "Price": 8999, "OS": "Android"},
		{"Model": "Samsung Galaxy M30", "Company": "Samsung", "RAM": 4, "Storage": 64, "BCapacity": 5000, "Price": 12999, "OS": "Android"},
		{"Model": "Samsung Galaxy M30", "Company": "Samsung", "RAM": 3, "Storage": 32, "BCapacity": 5000, "Price": 10999, "OS": "Android"}]


		window = Tk()
		window.geometry('640x480')
		window.title("Mobile Recommender")

		# Create menu bar
		menubar = Menu(window)
		window.config(menu = menubar) # Display the menu bar

		# Create a pull-down menu namely "Company" and add it to menu bar
		company_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Company", menu = company_menu)
		company_menu.add_command(label = "Samsung", command = partial(self.setCompany, "Samsung"))
		company_menu.add_command(label = "Xiomi", command = partial(self.setCompany, "Xiomi"))
		company_menu.add_command(label = "Apple", command = partial(self.setCompany, "Apple"))
		company_menu.add_command(label = "Asus", command = partial(self.setCompany, "Asus"))
		company_menu.add_command(label = "Oppo", command = partial(self.setCompany, "Oppo"))
		company_menu.add_command(label = "Huawei", command = partial(self.setCompany, "Huawei"))
		company_menu.add_command(label = "One Plus", command = partial(self.setCompany, "One Plus"))

		# Create a pull-down menu namely "RAM" and add it to menu bar
		ram_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "RAM", menu = ram_menu)
		ram_menu.add_command(label = "1 GB", command = partial(self.setRam, 1))
		ram_menu.add_command(label = "2 GB", command = partial(self.setRam, 2))
		ram_menu.add_command(label = "3 GB", command = partial(self.setRam, 3))
		ram_menu.add_command(label = "4 GB", command = partial(self.setRam, 4))
		ram_menu.add_command(label = "6 GB", command = partial(self.setRam, 6))
		ram_menu.add_command(label = "8 GB", command = partial(self.setRam, 8))

		# To open a new window
		def createNewWindow():
			self.getSpecification()
			window2 = Toplevel(window)
			window2.title("list")
			#window2.geometry("400x400")
			frame1 = Frame(window2)
			frame1.pack()
			if len(self.filtered) == 0:
				print("No record found")
				Label(frame1, text = "No record found in the database. Try selecting a different combination.").pack()
			else:
				for i in self.filtered:
					Label(frame1, text = "Model Name: " + i["Model"] + "\n" + "Company: " + i["Company"] + "\n" + "RAM" + str(i["RAM"])).pack()

		# Create a frame to show details of the filtered smarphones
		frame = Frame(window)
		frame.pack()

		# Create a button to show the details of filtered smartphones and add it to frame
		Button(frame, text = "Show", command = createNewWindow).pack()
		window.mainloop()

	def setCompany(self, company):
		self.company = company
		print("Company: ", self.company)

	def setRam(self, ram):
		self.ram = ram
		print("RAM: ", self.ram)

	def getSpecification(self):
		temp_filtered = []
		temp_filtered2 = []
		for i in self.specifications:
			if i["RAM"] >= self.ram:
				temp_filtered.append(i)
		for i in temp_filtered:
			if self.company != "":
				if i["Company"] == self.company:
					temp_filtered2.append(i)
					temp_filtered = []
		self.filtered = temp_filtered2

MobileRecommender()