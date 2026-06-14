# FFML

> This project has been replaced by https://github.com/tzimar/ffml-ts

FFML is a simple markup language combining aspects of BBCode and Markdown, designed for writing fanfics in a format that's flexible but that remains 'plain'. 

* Readable formatting (`*italics*`, `**bold**`, `_underline_`, `~strikethrough~`, `$small caps$`)
* Styled divs and spans (`[.center; Centered div]`, `<.red; Red span>`)
* Comments (`{ Annotate your writing however you want! }`)
* Escaped text (`` You're a `****`. ``)
* Multiple types of breaks (scene breaks, section breaks, line breaks)
* Automatic paragraph indentation
* Support for Polish dialogue (`= I hate you = she said hatefully. = I despise you.`)
* Metadata
  * Todos (`{!todo write this later!!!}`)
  * Chapter splitting (`{!chapter chapter-1}`)

## Usage

```
usage: render.py [-h] [--output OUTPUT] [--output-dir OUTPUT_DIR]
                 [--template TEMPLATE] [--config CONFIG] [--suppress-todos]
                 [--stat]
                 [source]

Render FFML to HTML

positional arguments:
  source                input file; reads from stdin if omitted

options:
  -h, --help            show this help message and exit
  --output OUTPUT, -o OUTPUT
                        output file; writes to stdout if omitted
  --output-dir OUTPUT_DIR, -d OUTPUT_DIR
                        directory for output files
  --template TEMPLATE, -t TEMPLATE
                        HTML template file with {{content}} placeholder
  --config CONFIG, -c CONFIG
                        JSON config file
  --suppress-todos      suppress todos
  --stat                show word count statistics
```

The generated HTML relies on CSS styling to display correctly. The stylesheet `style.css` is provided as an example.

## Config

The configuration file allows the user to customise aspects of the rendering. `config.json` in this repo is provided as an example and doesn't represent the defaults.

```jsonc
{
  "breaks": {
    "=": "<p class=\"hard-break\">&#x2731; &#x2731; &#x2731;</p>",  // scene break
    "-": "<p class=\"soft-break\"></p>",                            // break within scene
    ">": "<br class=\"line-break\">",                               // line break
    "<": "",                                                        // semantic, non-visible break
    "_": "<hr>"                                                     // divider break
  },
  "emphasis": {
    "***": "<b><i>{{content}}</i></b>",
    "**": "<b>{{content}}</b>",
    "*": "<i>{{content}}</i>",
    "_": "<u>{{content}}</u>",
    "~": "<s>{{content}}</s>",
    "$": "<span class=\"small-caps\">{{content}}</span>"
  },
  "entities": {
    "egyptian-cat": "&#x130e0;",
    "zwsp": "&#x200b;"
  }
}
```

---

Input-output example pairs are provided in the `examples` directory. Run `test.py` to test the renderer against these pairs.
