from tkinter import *
from functools import partial

class MobileRecommender:
	def __init__(self):
		self.company = ""
		self.ram = 0
		self.storage = 0
		self.capacity = 0
		self.price = 0
		self.os = ""
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
		window.geometry('400x300') # Specify the size of window in pixels
		window.title("Mobile Recommender") # Set the title of the new window

		# Create menu bar
		menubar = Menu(window) # Create a menubar
		window.config(menu = menubar) # Display the menu bar

		# Create a pull-down menu namely "Company" and add it to menu bar
		company_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Company", menu = company_menu)
		company_menu.add_command(label = "Samsung", command = partial(self.setCompany, "Samsung"))
		company_menu.add_command(label = "Google Pixel", command = partial(self.setCompany, "Google Pixel"))
		company_menu.add_command(label = "Apple", command = partial(self.setCompany, "Apple"))
		company_menu.add_command(label = "Asus", command = partial(self.setCompany, "Asus"))
		company_menu.add_command(label = "Xiomi", command = partial(self.setCompany, "Xiomi"))
		company_menu.add_command(label = "Huawei", command = partial(self.setCompany, "Huawei"))
		company_menu.add_command(label = "OnePlus", command = partial(self.setCompany, "OnePlus"))
		company_menu.add_command(label = "Sony", command = partial(self.setCompany, "Sony"))
		company_menu.add_command(label = "Oppo", command = partial(self.setCompany, "Oppo"))
		company_menu.add_command(label = "Vivo", command = partial(self.setCompany, "Vivo"))

		# Create a pull-down menu namely "RAM" and add it to menu bar
		ram_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "RAM", menu = ram_menu)
		ram_menu.add_command(label = "1 GB", command = partial(self.setRam, 1))
		ram_menu.add_command(label = "2 GB", command = partial(self.setRam, 2))
		ram_menu.add_command(label = "3 GB", command = partial(self.setRam, 3))
		ram_menu.add_command(label = "4 GB", command = partial(self.setRam, 4))
		ram_menu.add_command(label = "6 GB", command = partial(self.setRam, 6))
		ram_menu.add_command(label = "8 GB", command = partial(self.setRam, 8))

		# Create a pull-down menu namely "Storage" and add it to menu bar
		storage_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Storage", menu = storage_menu)
		storage_menu.add_command(label = "8 GB", command = partial(self.setStorage, 8))
		storage_menu.add_command(label = "16 GB", command = partial(self.setStorage, 16))
		storage_menu.add_command(label = "32 GB", command = partial(self.setStorage, 32))
		storage_menu.add_command(label = "64 GB", command = partial(self.setStorage, 64))
		storage_menu.add_command(label = "128 GB", command = partial(self.setStorage, 128))
		storage_menu.add_command(label = "256 GB", command = partial(self.setStorage, 256))

		# Create a pull-down menu namely "Battery Capacity" and add it to menu bar
		battery_capacity_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Battery Capacity", menu = battery_capacity_menu)
		battery_capacity_menu.add_command(label = "2000 mAh", command = partial(self.setBatteryCapacity, 2000))
		battery_capacity_menu.add_command(label = "3000 mAh", command = partial(self.setBatteryCapacity, 3000))
		battery_capacity_menu.add_command(label = "4000 mAh", command = partial(self.setBatteryCapacity, 4000))
		battery_capacity_menu.add_command(label = "5000 mAh", command = partial(self.setBatteryCapacity, 5000))
		battery_capacity_menu.add_command(label = "6000 mAh", command = partial(self.setBatteryCapacity, 6000))
		battery_capacity_menu.add_command(label = "7000 mAh", command = partial(self.setBatteryCapacity, 7000))
		battery_capacity_menu.add_command(label = "8000 mAh", command = partial(self.setBatteryCapacity, 8000))

		# Create a pull-down menu namely "Price" and add it to menu bar
		price_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Price", menu = price_menu)
		price_menu.add_command(label = "10000", command = partial(self.setPrice, 10000))
		price_menu.add_command(label = "15000", command = partial(self.setPrice, 10000))
		price_menu.add_command(label = "20000", command = partial(self.setPrice, 10000))
		price_menu.add_command(label = "30000", command = partial(self.setPrice, 10000))
		price_menu.add_command(label = "40000", command = partial(self.setPrice, 10000))
		price_menu.add_command(label = "50000", command = partial(self.setPrice, 10000))
		price_menu.add_command(label = "70000", command = partial(self.setPrice, 10000))
		price_menu.add_command(label = "100000", command = partial(self.setPrice, 10000))
		price_menu.add_command(label = "125000", command = partial(self.setPrice, 10000))
		price_menu.add_command(label = "150000", command = partial(self.setPrice, 10000))
		price_menu.add_command(label = "More", command = partial(self.setPrice, 150001))

		# Create a pull-down menu namely "OS" and add it to menu bar
		os_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "OS", menu = os_menu)
		os_menu.add_command(label = "Android", command = partial(self.setOS, "Android"))
		os_menu.add_command(label = "IOS", command = partial(self.setOS, "IOS"))

		# To open a new window to show the details of filtered smartphones
		def createNewWindow():
			self.getSpecification()
			window2 = Toplevel(window)
			window2.title("Mobile Recommendations")
			window2.geometry("500x650")
			mainframe = Frame(window2)
			canvas = Canvas(mainframe, width = 480, height = 650)
			scrollbar = Scrollbar(mainframe, orient = "vertical", command = canvas.yview)
			frame1 = Frame(canvas)
			frame1.bind("<Configure>", lambda e: canvas.configure(scrollregion = canvas.bbox("all")))
			canvas.create_window((0, 0), window = frame1, anchor = "nw")
			canvas.configure(yscrollcommand = scrollbar.set)
			mainframe.pack()
			canvas.pack(side = "left", fill = "both", expand = True)
			scrollbar.pack(side = "right", fill = "y")


			# If no record was found in the filtered list
			if len(self.filtered) == 0:
				print("No record found")
				no_record_found_label = Label(frame1, text = "No record found in the database. Try selecting a different combination.")
				no_record_found_label.pack()

			else: # If record was found
				row = 1 # To track the row in the grid manager
				colors = ["#ccccff", "#ffcc99", "#ffff99", "#ffcccc", "#ccffcc"]
				color = 0 # To assign different colors to each iteration of result
				for i in self.filtered:
					label1 = Label(frame1, text = "Model Name: ", font = "Times 16 bold", bg = colors[color])
					label1.grid(row = row, column = 1, sticky = W)
					label2 = Label(frame1, text = i["Model"], font = "Times 16", bg = colors[color])
					label2.grid(row = row, column = 2, sticky = W)
					row += 1
					label3 = Label(frame1, text = "Company: ", font = "Times 16 bold", bg = colors[color])
					label3.grid(row = row, column = 1, sticky = W)
					label4 = Label(frame1, text = i["Company"], font = "Times 16", bg = colors[color])
					label4.grid(row = row, column = 2, sticky = W)
					row += 1
					label5 = Label(frame1, text = "RAM: ", font = "Times 16 bold", bg = colors[color])
					label5.grid(row = row, column = 1, sticky = W)
					label6 = Label(frame1, text = str(i["RAM"]) + " GB", font = "Times 16", bg = colors[color])
					label6.grid(row = row, column = 2, sticky = W)
					row += 1
					label9 = Label(frame1, text = "Internal Storage: ", font = "Times 16 bold", bg = colors[color])
					label9.grid(row = row, column = 1, stick = W)
					label10 = Label(frame1, text = str(i["Storage"]) + " GB", font = "Times 16", bg = colors[color])
					label10.grid(row = row, column = 2, sticky = W)
					row += 1
					label7 = Label(frame1, text = "Battery Capacity: ", font = "Times 16 bold", bg = colors[color])
					label7.grid(row = row, column = 1, sticky = W)
					label8 = Label(frame1, text = str(i["BCapacity"]) + " mAh", font = "Times 16", bg = colors[color])
					label8.grid(row = row, column = 2, sticky = W)
					row += 1
					label11 = Label(frame1, text = "Price: ", font = "Times 16 bold", bg = colors[color])
					label11.grid(row = row, column = 1, sticky = W)
					label12 = Label(frame1, text = "Rs. " + str(i["Price"]), font = "Times 16", bg = colors[color])
					label12.grid(row = row, column = 2, sticky = W)
					row += 1
					label13 = Label(frame1, text = "OS: ", font = "Times 16 bold", bg = colors[color])
					label13.grid(row = row, column = 1, sticky = W)
					label14 = Label(frame1, text = i["OS"], font = "Times 16", bg = colors[color])
					label14.grid(row = row, column = 2, sticky = W)
					row += 1
					labelline1 = Label(frame1, text = "_________________________________")
					labelline2 = Label(frame1, text = "_________________________________")
					labelline1.grid(row = row, column = 1)
					labelline2.grid(row = row, column = 2)
					row += 1
					if color == 4: # If color is the last color, then set it to first color
						color = 0
					else:
						color += 1 # Otherwise set color to next color


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
		print("RAM: ", self.ram, "GB")

	def setStorage(self, storage):
		self.storage = storage
		print("Internal Storage: ", self.storage, "GB")

	def setBatteryCapacity(self, capacity):
		self.capacity = capacity
		print("Battery Capacity: ", self.capacity, "mAh")

	def setPrice(self, price):
		self.price = price;
		print("Price: ", self.price)

	def setOS(self, os):
		self.os = os
		print("OS: ", os)

	# To filter data and put final filtered data into self.filtered
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