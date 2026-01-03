# Curly

## Description

This Bash script allows you to enumerate routes over a specific URL. The script sends HTTP requests to all routes specified in a route list file and displays the results based on the chosen parameters. You can view the response content or just the HTTP status code.

## Arguments

The following arguments are accepted by the script:

- **`-u <url>`**: The base URL to which the routes from the file will be added.
  - Example: `-u https://www.example.com`
  
- **`-l <route_list>`**: The text file that contains the routes to be enumerated.
  - Example: `-l routes.txt`
  
- **`-c`**: Display the HTTP response content (default).
  
- **`-s`**: Display only the HTTP status code of the response.
  
- **`-h`**: Show the help message with the available arguments.


## Installation

1. **Clone the repository**:

   First, clone the repository to your local machine:

   ```bash
   git clone https://github.com/pablo-972/Curly
   cd curly
   ```

2. **Grant execution permissions**:

   To execute the script, ensure that it has execution permissions:

   ```bash
   chmod +x curly.sh
   ```

## Basic Usage

Once the script is ready, you can run the route enumeration with the following basic command:

```bash
./curly.sh -u <url> -l <route_list> [-c] [-s]
```


## Advanced Example:

If you want to see the response content and search for certain keywords (like "pass", "user", or "name") within those responses, you can use the following command:

```bash
./curly.sh -u 'https://www.example.com' -l routes.txt [-c] | grep -E "pass|user|name"
```

This will do the following:
1. It will search the content of each enumerated route in `routes.txt`.
2. It will use `grep` to search for the keywords "pass", "user", or "name" in the responses.
