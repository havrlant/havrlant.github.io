from glob import glob

import xml.etree.ElementTree as ET

for filepath in glob("**/*.svg") + glob("*.svg"):
	tree = ET.parse(filepath)
	root = tree.getroot()

	for child in tree.findall('.//{http://www.w3.org/2000/svg}switch'):
		textNode = child.find(".//{http://www.w3.org/2000/svg}text")
		if textNode.text == "[Not supported by viewer]":
			textNode.text = child.find(".//{http://www.w3.org/2000/svg}foreignObject/{http://www.w3.org/1999/xhtml}div/{http://www.w3.org/1999/xhtml}div").text

	tree.write(filepath)
