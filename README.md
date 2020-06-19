# Random nhentai Finder
Find random nhentai based on tags!

## Installation
#### Clone
- Clone this repo to your local machine using ```https://github.com/TacoAnime69/RandomNhentai```

## Running the Script
> Navigate to the repo directory on your local machine. Then execute the following:
```
$ python3 RandomHentai.py
```
Follow `RandomHentai.py` with the desired arguments.

## Usage
### Basic Usage
No arguments: this will result in a completely random doujin with no restrictions.

Example:
```
python3 RandomHentai.py
```

### Search All Tag Types
All tags behave the same way as searching on nhentai website. You can list tags, characters, parodies, and languages. All arguments are searched with 'and' arguments. 

Example: 
```
python3 RandomHentai.py yuri big-breast english
```
Result: A random doujin that has the tags yuri and big breast in English language.
> Note: any tags/searches that has a space in it needs to be replaced with a '-'

### Negate Search
To specify tags of any type to exclude in the search, add '-' in front.

Example: 
```
python3 RandomHentai.py blowjob -rape -chinese
```
Result: A random doujin with the tag blowjob but not rape and that is NOT in the Chinese language.

### Advanced Tag Type Search
There may be some cases where you need to specify a parameter, in which case you can type '[parameter namee]:[argument]'

Example: 
```
python3 RandomHentai.py yuri 'pages:>20' 'tag:"big breast"' 'parodies:"bang dream"'
```
Result: A random doujin with the tag yuri that's greater than 20 pages with the tag big breast that porodies big dream.

### Optional Flags
```--help``` - shows this help text.

```--browser``` - will open your default browser to the doujin.

```--all``` - will display detailed info on the random doujin.

## Contributing
You are welcome to contribute to this as you'd like!

## Support

Feel free to reach out if you have any questions!
> If you want to report a bug, please check out __Issues__ and only use email.
- Email: hentai.boi@outlook.com
- Twitter at [@TacoAnime69](https://twitter.com/TacoAnime69)
