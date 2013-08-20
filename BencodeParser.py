import sublime, sublime_plugin
import bencode

class ParseBencodeCommand(sublime_plugin.WindowCommand):
	def run(self):
		view = self.window.active_view()
		file_contents = view.substr(sublime.Region(0, view.size()))
		f = self.window.new_file()
		f.set_syntax_file('Packages/Python/Python.tmLanguage')
		edit = f.begin_edit()
		f.insert(edit, 0, str(bencode.bdecode(file_contents)))
