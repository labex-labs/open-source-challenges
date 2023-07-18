# Temporary Files and Directories

## Introduction

In programming, we often need to create data that is not needed after the program exits. Temporary files and directories are useful for this purpose since they do not pollute the file system over time.

In this lab, you need to create temporary files and directories in Go.

- Use `os.CreateTemp` to create a temporary file.
- Use `os.MkdirTemp` to create a temporary directory.
- Use `os.RemoveAll` to remove the temporary directory.
- Use `os.WriteFile` to write data to a file.

## TODO

```go
// The easiest way to create a temporary file is by
// calling `os.CreateTemp`. It creates a file *and*
// opens it for reading and writing. We provide `""`
// as the first argument, so `os.CreateTemp` will
// create the file in the default location for our OS.
f, err := os.CreateTemp("", "sample")
check(err)

// Display the name of the temporary file. On
// Unix-based OSes the directory will likely be `/tmp`.
// The file name starts with the prefix given as the
// second argument to `os.CreateTemp` and the rest
// is chosen automatically to ensure that concurrent
// calls will always create different file names.
fmt.Println("Temp file name:", f.Name())

// Clean up the file after we're done. The OS is
// likely to clean up temporary files by itself after
// some time, but it's good practice to do this
// explicitly.
defer os.Remove(f.Name())

// We can write some data to the file.
_, err = f.Write([]byte{1, 2, 3, 4})
check(err)

// If we intend to write many temporary files, we may
// prefer to create a temporary *directory*.
// `os.MkdirTemp`'s arguments are the same as
// `CreateTemp`'s, but it returns a directory *name*
// rather than an open file.
dname, err := os.MkdirTemp("", "sampledir")
check(err)
fmt.Println("Temp dir name:", dname)

defer os.RemoveAll(dname)

// Now we can synthesize temporary file names by
// prefixing them with our temporary directory.
fname := filepath.Join(dname, "file1")
err = os.WriteFile(fname, []byte{1, 2}, 0666)
check(err)
```

```
Temp file name: /tmp/sample123456
Temp dir name: /tmp/sampledir123456
```

## Summary

In this lab, you learned how to create temporary files and directories in Go using `os.CreateTemp`, `os.MkdirTemp`, `os.RemoveAll`, and `os.WriteFile`. Temporary files and directories are useful for creating data that is not needed after the program exits and do not pollute the file system over time.
