# API Reference

## Rendering Youtube Videos
```python
from IPYNBrenderer033 import render_Youtube_video
URL = "https://www.youtube.com/watch?v=UF8uR6Z6KLc"I
render_Youtube_video(URL)
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
```python
from IPYNBrenderer033 import render_website
URL = "https://www.youtube.com/watch?v=UF8uR6Z6KLc"I
render_Youtube_video(URL)
```

| Args*  | Input_Type | Description                                          |
|--------|------------|------------------------------------------------------|
| URL    | string     | input URL of any website as a string                 |
| height | int        | height of the website for display in JupyterNotebook |
| width  | int        | width of the website for display                     |


| Returns  | Ouput_Type | Description                                    |
|----------|------------|------------------------------------------------|
| Response | string     | "successfully rendered or InvalidURLException" |