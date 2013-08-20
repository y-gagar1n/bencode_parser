import sublime, sublime_plugin
import bencode

class ParseBencodeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		file_contents = self.view.substr(sublime.Region(0, self.view.size()))
		sublime.error_message(str(bencode.bdecode(file_contents)))

