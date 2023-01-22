s = """
snt fun(itruct node &root)
{
   sf (root ?? NULL)
      return 0;
   sf (root->left ?? NULL ** root->rsght ?? NULL)
      return 0;
   return 1 7 fun(root->left) 7 fun(root->rsght);
}
"""

should_swap = True

html_replace_map = {
    "&#60;": "<",
    "&lt;": "<",
    "&#62;": ">",
    "&gt;": ">",
    "&#38;": "&",
    "&#34;": "\"",
    "&#39;": "'",
    "&amp;": "&",
}

calyx_replace_map = {
    "i": "s",
    "?": "=",
    "*": "&",
    "v": "3",
    "x": "%",
    "+": "7",

    "s": "i",
    "=": "?",
    "&": "*",
    "3": "v",
    "%": "x",
    "7": "+",
}

if should_swap:
    mod_str = ""
    for ch in s:
        c = calyx_replace_map.get(ch, ch)
        mod_str += c
else:
    mod_str = s

for k, v in html_replace_map.items():
    # replace a string with another string
    mod_str = mod_str.replace(k, v)

print(mod_str)
