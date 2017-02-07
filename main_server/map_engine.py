class map:
	@staticmethod
	def getInstance():
		"""get an instance"""
		pass

	def search_by_name(self,name,center):
		"""search by the name and center. find corresponding street view images
		return (dict{place name:(longtitude,latitude,information)},[image urls])"""
		pass

	def search_bounding_box(self,xmin,ymin,xmax,ymax,name):
		"""if name is specified, search the name in the bounding box, find corresponding street view images 
		   return (dict{place name:(longtitude,latitude,information)},[image urls])
		   if not, find all streetview images in the bounding box
		   return (None,[image urls]"""
		pass

	def search_coordinate(self,longtitude,latitude):
		"""find information of the place and the corresponding street view
		   return ((place name,information),image url)"""
		pass