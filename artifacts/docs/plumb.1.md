# plumb(1) — send messages to the plumber

## Synopsis

`plumb` [**-d**] [**-i** _srcdir_] [**-s** _plumbport_] [**-a** _attr=val_ ...] [**-w** _winid_] [**-p** _plumber_]

## Description

**Plumb** sends messages to the plumber(4) for routing. The message is read from standard input or constructed from the command line arguments. The message is sent to the named port, or to the default port if none is specified. The options are:

- **-d**: Print debugging information.
- **-i** _srcdir_: Set the source directory for the message.
- **-s** _plumbport_: Set the destination port for the message.
- **-a** _attr=val_: Add an attribute to the message.
- **-w** _winid_: Set the window id for the message.
- **-p** _plumber_: Use the specified plumber instead of the default.

If no message is provided, **plumb** reads a message from standard input.

## Examples

Send a message to the edit port:

```sh
echo 'data=main.c' | plumb -s edit
```

Send a message with attributes:

```sh
plumb -s edit -a data=main.c -a addr=23
```

## Files

- `/mnt/plumb` — default plumber mount point

## See Also

- [plumber(4)](plumber.4.md)

## Source

Plan 9 from User Space

## Bugs

The interface is subject to change.

