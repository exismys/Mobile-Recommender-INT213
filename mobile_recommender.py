from tkinter import *
from functools import partial

class MobileRecommender:
	def __init__(self):
		self.company = None
		self.ram = 0
		self.storage = 0
		self.capacity = 0
		self.price = None
		self.os = None
		self.filtered = []

		# Store smartphone data in a list
		self.specifications = [
		{"Model": "Apple iPhone 8 Plus", "Company": "Apple", "RAM": 2, "Storage": 256, "BCapacity": 2691, "Price": 46130, "OS": "iOS"},
		{"Model": "Samsung Galaxy M10s", "Company": "Samsung", "RAM": 3, "Storage": 32, "BCapacity": 4000, "Price": 8999, "OS": "Android"},
		{"Model": "Samsung Galaxy M30", "Company": "Samsung", "RAM": 4, "Storage": 64, "BCapacity": 5000, "Price": 12999, "OS": "Android"},
		{"Model": "Samsung Galaxy M30", "Company": "Samsung", "RAM": 3, "Storage": 32, "BCapacity": 5000, "Price": 10999, "OS": "Android"},
		{"Model": "Samsung Galaxy S20 Ultra", "Company": "Samsung", "RAM": 12, "Storage": 128, "BCapacity": 5000, "Price": 92999, "OS": "Android"},
		{"Model": "Samsung Galaxy S20 FE", "Company": "Samsung", "RAM": 8, "Storage": 128, "BCapacity": 4500, "Price": 49999, "OS": "Android"},
		{"Model": "Samsung Galaxy S20", "Company": "Samsung", "RAM": 8, "Storage": 128, "BCapacity": 4000, "Price": 65499, "OS": "Android"},
		{"Model": "Samsung Galaxy A31", "Company": "Samsung", "RAM": 6, "Storage": 128, "BCapacity": 5000, "Price": 19999, "OS": "Android"},
		{"Model": "Samsung Galaxy A21s", "Company": "Samsung", "RAM": 4, "Storage": 64, "BCapacity": 5000, "Price": 14999, "OS": "Android"},
		{"Model": "Samsung Galaxy Note 10 Plus", "Company": "Samsung", "RAM": 12, "Storage": 256, "BCapacity": 4300, "Price": 59999, "OS": "Android"},
		{"Model": "Apple iPhone 12 Mini", "Company": "Apple", "RAM": 4, "Storage": 256, "BCapacity": 2227, "Price": 69900, "OS": "iOS"},
		{"Model": "Apple iPhone 12 Pro Max", "Company": "Apple", "RAM": 6, "Storage": 512, "BCapacity": 3687, "Price": 129900, "OS": "iOS"},
		{"Model": "Apple iPhone 12", "Company": "Apple", "RAM": 4, "Storage": 256, "BCapacity": 2851, "Price": 79900, "OS": "iOS"},
		{"Model": "Apple iPhone SE", "Company": "Apple", "RAM": 3, "Storage": 64, "BCapacity": 1821, "Price": 32999, "OS": "iOS"},
		{"Model": "Apple iPhone 11", "Company": "Apple", "RAM": 4, "Storage": 64, "BCapacity": 3110, "Price": 49999, "OS": "iOS"},
		{"Model": "Samsung Galaxy M30s", "Company": "Samsung", "RAM": 4, "Storage": 64, "BCapacity": 6000, "Price": 13999, "OS": "Android"},
		{"Model": "Samsung Galaxy M51", "Company": "Samsung", "RAM": 6, "Storage": 128, "BCapacity": 7000, "Price": 22499, "OS": "Android"},
		{"Model": "Samsung Galaxy M31", "Company": "Samsung", "RAM": 6, "Storage": 64, "BCapacity": 6000, "Price": 15499, "OS": "Android"},
		{"Model": "Samsung Galaxy M11", "Company": "Samsung", "RAM": 3, "Storage": 32, "BCapacity": 5000, "Price": 9399, "OS": "Android"},
		{"Model": "Apple iPhone 11 Pro", "Company": "Apple", "RAM": 6, "Storage": 64, "BCapacity": 3190, "Price": 79999, "OS": "iOS"},
		{"Model": "Apple iPhone X", "Company": "Apple", "RAM": 3, "Storage": 64, "BCapacity": 2716, "Price": 57999, "OS": "iOS"},
		{"Model": "Google Pixel 4A", "Company": "Google Pixel", "RAM": 6, "Storage": 128, "BCapacity": 2140, "Price": 31999, "OS": "Android"},
		{"Model": "Google Pixel 3A", "Company": "Google Pixel", "RAM": 4, "Storage": 64, "BCapacity": 3000, "Price": 30999, "OS": "Android"},
		{"Model": "Google Pixel 3", "Company": "Google Pixel", "RAM": 4, "Storage": 64, "BCapacity": 2915, "Price": 71000, "OS": "Android"},
		{"Model": "Huawei Y9s", "Company": "Huawei", "RAM": 6, "Storage": 128, "BCapacity": 4000, "Price": 19900, "OS": "Android"},
		{"Model": "Huawei P30 Lite", "Company": "Huawei", "RAM": 4, "Storage": 128, "BCapacity": 3340, "Price": 16055, "OS": "Android"},
		{"Model": "Huawei P30 Pro", "Company": "Huawei", "RAM": 8, "Storage": 256, "BCapacity": 4200, "Price": 56490, "OS": "Android"},
		{"Model": "Huawei Mate 20 Pro", "Company": "Huawei", "RAM": 6, "Storage": 128, "BCapacity": 4200, "Price": 31999, "OS": "Android"},
		{"Model": "OnePlus 8T", "Company": "OnePlus", "RAM": 12, "Storage": 256, "BCapacity": 4500, "Price": 42999, "OS": "Android"},
		{"Model": "Redmi 9i", "Company": "Xiaomi", "RAM": 4, "Storage": 64, "BCapacity": 5000, "Price": 8299, "OS": "Android"},
		{"Model": "Redmi Note 8", "Company": "Xiaomi", "RAM": 4, "Storage": 64, "BCapacity": 4000, "Price": 11499, "OS": "Android"},
		{"Model": "Sony Xperia L2", "Company": "Sony", "RAM": 3, "Storage": 32, "BCapacity": 3300, "Price": 15900, "OS": "Android"},
		{"Model": "Sony Xperia XZ2", "Company": "Sony", "RAM": 6, "Storage": 64, "BCapacity": 3180, "Price": 74990, "OS": "Android"},
		{"Model": "Sony Xperia R1", "Company": "Sony", "RAM": 2, "Storage": 16, "BCapacity": 2620, "Price": 9990, "OS": "Android"},
		{"Model": "OPPO A33", "Company": "OPPO", "RAM": 3, "Storage": 32, "BCapacity": 5000, "Price": 11990, "OS": "Android"},
		{"Model": "Vivo Y20", "Company": "Vivo", "RAM": 4, "Storage": 64, "BCapacity": 5000, "Price": 12990, "OS": "Android"}]

		window = Tk()
		window.geometry('400x350') # Specify the size of window in pixels
		window.title("Mobile Recommender") # Set the title of the new window

		# Create menu bar
		menubar = Menu(window) # Create a menubar
		window.config(menu = menubar) # Display the menu bar

		# Create a frame to show details of the filtered smarphones
		frame = Frame(window)
		frame.pack()

		# Show the user selection data in frame
		Label(frame, text = "").grid(row = 1, column = 1)
		def updateSelectionData():
			row = 2
			colors = ["#ccccff", "#ffcc99", "#ffff99", "#ffcccc", "#ccffcc"]
			color = 0 # To assign different colors to each iteration of result
			label3 = Label(frame, text = "Company: ", font = "Times 16 bold", bg = colors[color])
			label3.grid(row = row, column = 1, sticky = W)
			label4 = Label(frame, text = self.company, font = "Times 16", bg = colors[color])
			label4.grid(row = row, column = 2, sticky = W)
			row += 1
			color += 1
			label5 = Label(frame, text = "Minimum RAM: ", font = "Times 16 bold", bg = colors[color])
			label5.grid(row = row, column = 1, sticky = W)
			label6 = Label(frame, text = str(self.ram) + " GB", font = "Times 16", bg = colors[color])
			label6.grid(row = row, column = 2, sticky = W)
			row += 1
			color += 1
			label9 = Label(frame, text = "Minimum Internal Storage: ", font = "Times 16 bold", bg = colors[color])
			label9.grid(row = row, column = 1, stick = W)
			label10 = Label(frame, text = str(self.storage) + " GB", font = "Times 16", bg = colors[color])
			label10.grid(row = row, column = 2, sticky = W)
			row += 1
			color += 1
			label7 = Label(frame, text = "Minimum Battery Capacity: ", font = "Times 16 bold", bg = colors[color])
			label7.grid(row = row, column = 1, sticky = W)
			label8 = Label(frame, text = str(self.capacity) + " mAh", font = "Times 16", bg = colors[color])
			label8.grid(row = row, column = 2, sticky = W)
			row += 1
			color += 1
			label11 = Label(frame, text = "Price: (Under)", font = "Times 16 bold", bg = colors[color])
			label11.grid(row = row, column = 1, sticky = W)
			label12 = Label(frame, text = str(self.price), font = "Times 16", bg = colors[color])
			label12.grid(row = row, column = 2, sticky = W)
			row += 1
			color = 0
			label13 = Label(frame, text = "OS: ", font = "Times 16 bold", bg = colors[color])
			label13.grid(row = row, column = 1, sticky = W)
			label14 = Label(frame, text = self.os, font = "Times 16", bg = colors[color])
			label14.grid(row = row, column = 2, sticky = W)
		updateSelectionData()

		# Create a pull-down menu namely "Company" and add it to menu bar
		company_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Company", menu = company_menu)
		company_menu.add_command(label = "Samsung", command = lambda: [self.setCompany("Samsung"), updateSelectionData()])
		company_menu.add_command(label = "Google Pixel", command = lambda: [self.setCompany("Google Pixel"), updateSelectionData()])
		company_menu.add_command(label = "Apple", command = lambda: [self.setCompany("Apple"), updateSelectionData()])
		company_menu.add_command(label = "Asus", command = lambda: [self.setCompany("Asus"), updateSelectionData()])
		company_menu.add_command(label = "Xiomi", command = lambda: [self.setCompany("Xiomi"), updateSelectionData()])
		company_menu.add_command(label = "Huawei", command = lambda: [self.setCompany("Huawei"), updateSelectionData()])
		company_menu.add_command(label = "OnePlus", command = lambda: [self.setCompany("OnePlus"), updateSelectionData()])
		company_menu.add_command(label = "Sony", command = lambda: [self.setCompany("Sony"), updateSelectionData()])
		company_menu.add_command(label = "Oppo", command = lambda: [self.setCompany("Oppo"), updateSelectionData()])
		company_menu.add_command(label = "Vivo", command = lambda: [self.setCompany("Vivo"), updateSelectionData()])

		# Create a pull-down menu namely "RAM" and add it to menu bar
		ram_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "RAM", menu = ram_menu)
		ram_menu.add_command(label = "1 GB", command = lambda : [self.setRam(1), updateSelectionData()])
		ram_menu.add_command(label = "2 GB", command = lambda : [self.setRam(2), updateSelectionData()])
		ram_menu.add_command(label = "3 GB", command = lambda : [self.setRam(3), updateSelectionData()])
		ram_menu.add_command(label = "4 GB", command = lambda : [self.setRam(4), updateSelectionData()])
		ram_menu.add_command(label = "6 GB", command = lambda : [self.setRam(6), updateSelectionData()])
		ram_menu.add_command(label = "8 GB", command = lambda : [self.setRam(8), updateSelectionData()])

		# Create a pull-down menu namely "Storage" and add it to menu bar
		storage_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Storage", menu = storage_menu)
		storage_menu.add_command(label = "8 GB", command = lambda: [self.setStorage(8), updateSelectionData()])
		storage_menu.add_command(label = "16 GB", command = lambda: [self.setStorage(16), updateSelectionData()])
		storage_menu.add_command(label = "32 GB", command = lambda: [self.setStorage(32), updateSelectionData()])
		storage_menu.add_command(label = "64 GB", command = lambda: [self.setStorage(64), updateSelectionData()])
		storage_menu.add_command(label = "128 GB", command = lambda: [self.setStorage(128), updateSelectionData()])
		storage_menu.add_command(label = "256 GB", command = lambda: [self.setStorage(256), updateSelectionData()])

		# Create a pull-down menu namely "Battery Capacity" and add it to menu bar
		battery_capacity_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Battery Capacity", menu = battery_capacity_menu)
		battery_capacity_menu.add_command(label = "2000 mAh", command = lambda : [self.setBatteryCapacity(2000), updateSelectionData()])
		battery_capacity_menu.add_command(label = "3000 mAh", command = lambda : [self.setBatteryCapacity(3000), updateSelectionData()])
		battery_capacity_menu.add_command(label = "4000 mAh", command = lambda : [self.setBatteryCapacity(4000), updateSelectionData()])
		battery_capacity_menu.add_command(label = "5000 mAh", command = lambda : [self.setBatteryCapacity(5000), updateSelectionData()])
		battery_capacity_menu.add_command(label = "6000 mAh", command = lambda : [self.setBatteryCapacity(6000), updateSelectionData()])
		battery_capacity_menu.add_command(label = "7000 mAh", command = lambda : [self.setBatteryCapacity(7000), updateSelectionData()])
		battery_capacity_menu.add_command(label = "8000 mAh", command = lambda : [self.setBatteryCapacity(8000), updateSelectionData()])

		# Create a pull-down menu namely "Price" and add it to menu bar
		price_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "Price", menu = price_menu)
		price_menu.add_command(label = "10000", command = lambda: [self.setPrice(10000), updateSelectionData()])
		price_menu.add_command(label = "15000", command = lambda: [self.setPrice(15000), updateSelectionData()])
		price_menu.add_command(label = "20000", command = lambda: [self.setPrice(20000), updateSelectionData()])
		price_menu.add_command(label = "30000", command = lambda: [self.setPrice(30000), updateSelectionData()])
		price_menu.add_command(label = "40000", command = lambda: [self.setPrice(40000), updateSelectionData()])
		price_menu.add_command(label = "50000", command = lambda: [self.setPrice(50000), updateSelectionData()])
		price_menu.add_command(label = "70000", command = lambda: [self.setPrice(70000), updateSelectionData()])
		price_menu.add_command(label = "100000", command = lambda: [self.setPrice(100000), updateSelectionData()])
		price_menu.add_command(label = "125000", command = lambda: [self.setPrice(125000), updateSelectionData()])
		price_menu.add_command(label = "150000", command = lambda: [self.setPrice(150000), updateSelectionData()])
		price_menu.add_command(label = "More", command = lambda: [self.setPrice(150000), updateSelectionData()])

		# Create a pull-down menu namely "OS" and add it to menu bar
		os_menu = Menu(menubar, tearoff = 0)
		menubar.add_cascade(label = "OS", menu = os_menu)
		os_menu.add_command(label = "Android", command = lambda : [self.setOS("Android"), updateSelectionData()])
		os_menu.add_command(label = "IOS", command = lambda: [self.setOS("IOS"), updateSelectionData()])

		# To open a new window to show the details of filtered smartphones
		def createNewWindow():
			self.getSpecification()
			window2 = Toplevel(window)
			window2.title("Results")
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

		# Create a button to show the details of filtered smartphones and add it to frame
		Label(frame, text = "").grid(row = 8, column = 1)
		Button(frame, text = "Show", command = createNewWindow).grid(row = 9, column = 2)

		# Create frame2 to put "How to: "
		frame2 = Frame(window)
		frame2.pack()
		Label(frame2, text = "").pack()
		Label(frame2, text = "How To", font = "Times 13 bold").pack()
		Label(frame2, text = "Please choose specifictions from menus in menu bar and then click on \"Show\" button to see your mobile Recommendations.", wraplength = 380).pack()

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
		filtered_data1 = []
		filtered_data2 = []
		data_track = 0
		if self.company != None:
			if data_track == 0:
				for i in self.specifications:
					if i["Company"] == self.company:
						filtered_data1.append(i)
				data_track = 1
			elif data_track == 1:
				for i in filtered_data1:
					if i["Company"] == self.company:
						filtered_data2.append(i)
				filtered_data1 = []
				data_track = 2
			else:
				for i in filtered_data2:
					if i["Company"] == self.company:
						filtered_data1.append(i)
				filtered_data2 = []
				data_track = 1

		if self.ram != 0:
			if data_track == 0:
				for i in self.specifications:
					if i["RAM"] >= self.ram:
						filtered_data1.append(i)
				data_track = 1
			elif data_track == 1:
				for i in filtered_data1:
					if i["RAM"] >= self.ram:
						filtered_data2.append(i)
				filtered_data1 = []
				data_track = 2
			else:
				for i in filtered_data2:
					if i["RAM"] >= self.ram:
						filtered_data1.append(i)
				filtered_data2 = []
				data_track = 1

		if self.storage != 0:
			if data_track == 0:
				for i in self.specifications:
					if i["Storage"] >= self.storage:
						filtered_data1.append(i)
				data_track = 1
			elif data_track == 1:
				for i in filtered_data1:
					if i["Storage"] >= self.storage:
						filtered_data2.append(i)
				filtered_data1 = []
				data_track = 2
			else:
				for i in filtered_data2:
					if i["Storage"] >= self.storage:
						filtered_data1.append(i)
				filtered_data2 = []
				data_track = 1

		if self.capacity != 0:
			if data_track == 0:
				for i in self.specifications:
					if i["BCapacity"] >= self.capacity:
						filtered_data1.append(i)
				data_track = 1
			elif data_track == 1:
				for i in filtered_data1:
					if i["BCapacity"] >= self.capacity:
						filtered_data2.append(i)
				filtered_data1 = []
				data_track = 2
			else:
				for i in filtered_data2:
					if i["BCapacity"] >= self.capacity:
						filtered_data1.append(i)
				filtered_data2 = []
				data_track = 1

		if self.price != None:
			if data_track == 0:
				for i in self.specifications:
					if i["Price"] <= self.price:
						filtered_data1.append(i)
				data_track = 1
			elif data_track == 1:
				for i in filtered_data1:
					if i["Price"] <= self.price:
						filtered_data2.append(i)
				filtered_data1 = []
				data_track = 2
			else:
				for i in filtered_data2:
					if i["Price"] <= self.price:
						filtered_data1.append(i)
				filtered_data2 = []
				data_track = 1

		if self.os != None:
			if data_track == 0:
				for i in self.specifications:
					if i["OS"] == self.os:
						filtered_data1.append(i)
				data_track = 1
			elif data_track == 1:
				for i in filtered_data1:
					if i["OS"] == self.os:
						filtered_data2.append(i)
				filtered_data1 = []
				data_track = 2
			else:
				for i in filtered_data2:
					if i["OS"] == self.os:
						filtered_data1.append(i)
				filtered_data2 = []
				data_track = 1

		if data_track == 0:
			self.filtered = self.specifications
		elif data_track == 1:
			self.filtered = filtered_data1
		else:
			self.filtered = filtered_data2

MobileRecommender()
