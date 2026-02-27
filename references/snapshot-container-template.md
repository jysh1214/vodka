# Container Template

Template for capturing container environment information.

## Fields

| Field | Label | Example |
|---|---|---|
| Dockerfile path | `[container/name:dockerfile]` | `./Dockerfile` |
| Startup command | `[container/name:startup]` | `docker run -v $(pwd):/work myimage` |
| Image name | `[container/name:image]` | `myimage:latest` |

## Example

```txt
[container/myimage:dockerfile] ./Dockerfile
[container/myimage:startup] docker run -v $(pwd):/work myimage
[container/myimage:image] myimage:latest
```
