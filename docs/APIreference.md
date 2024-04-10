# API Reference

## Rendering Youtube Videos
??? note "Example code"
    ```python
    from IPYNBrenderer033 import render_Youtube_video
    URL = "https://www.youtube.com/watch?v=UF8uR6Z6KLc"I
    render_YouTube_video(URL=URL, width = 780, height = 480) 
    ```

| Args*   | Input_Type | Description                          |
|--------|------------|--------------------------------------|
| URL    | string     | URL of any youtube video as a string |
| height | int        | height the video for displaying      |
| width  | int        | width of the video for displaying    |

| Returns  | Ouput_Type | Description                                    |
|----------|------------|------------------------------------------------|
| Response | string     | "successfully rendered or InvalidURLException" |

## Rendering Reference Websites
??? note "Example code"
    ```python
    from IPYNBrenderer033 import render_website
    URL = ""http://pytorch.org/"
    render_site(URL = URL, width = "90%", height = "500") 
    ```

| Args*  | Input_Type | Description                                          |
|--------|------------|------------------------------------------------------|
| URL    | string     | input URL of any website as a string                 |
| height | string        | height of the website for display in JupyterNotebook |
| width  | string        | width of the website for display                     |


| Returns  | Ouput_Type | Description                                    |
|----------|------------|------------------------------------------------|
| Response | string     | "successfully rendered or InvalidURLException" |