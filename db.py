import collections.abc
import json
from abc import ABC
from os import listdir, remove, getcwd, path, makedirs
import collections.abc

class WatchedList(list, ABC):
	def __init__(self, val, db, key):
		super().__init__(val)
		self.db = db
		self.key = key

	def append(self, val):
		super().append(val)
		self.db[self.key] = self
		return self

	def remove(self, val):
		super().remove(val)
		self.db[self.key] = self
		return self

class WatchedDict(dict, ABC):
	def __init__(self, val, db, key):
		super().__init__(val)
		self.db = db
		self.key = key

	def __setitem__(self, key, value):
		super().__setitem__(key, value)
		self.db[self.key] = self

	def __getitem__(self, key):
		if key in self.keys():
			if type(self.get(key)) == dict:
				return WatchedDict(self.get(key), self, key)
			elif type(self.get(key)) == list:
				return WatchedList(self.get(key), self, key)
			else:
				return self.get(key)
		else:
			raise KeyError(key)


class Database(ABC):
	def __init__(self, dir):
		self.dir = dir
		"""
		if not path.exists(getcwd() + '/' + self.dir):
			try:
				makedirs(getcwd() + '/' + self.dir)
				print(f"[INFO] That directory ({self.dir}) didn't exist, it is created now.")
			except:
				pass
		"""
		try:
			makedirs(self.dir)
			print(f"[INFO] That directory ({self.dir}) didn't exist; it is created now.")
		except FileExistsError:
			pass

	def __setitem__(self, key, value):
		try:
			towrite = json.dumps(value.jsonify())
		except AttributeError:
			towrite = json.dumps(value)

		with open(f'{self.dir}/{key}', 'w+') as f:
			f.write(towrite)

	def __getitem__(self, key):
		if key in self.keys():
			with open(f'{self.dir}/{key}', 'r') as f:
				val = json.loads(f.read())
			if type(val) is list:
				return WatchedList(val, self, key)
			elif type(val) is dict:
				return WatchedDict(val, self, key)
			else:
				return val
		else:
			raise KeyError(key)

	def __delitem__(self, key):
		if key in self.keys():
			remove(f'{self.dir}/{key}')
		else:
			raise KeyError(key)

	def keys(self):
		return set(listdir(f'{self.dir}/'))

	def values(self):
		return [self[key] for key in self.keys()]