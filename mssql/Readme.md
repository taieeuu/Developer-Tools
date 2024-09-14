## USAGE

The sqlcmd has already been set as an environment variable and can be used directly.

- login

```sh
sqlcmd -S localhost -U sa -P !Root1234
```

- create db

```sh
CREATE DATABASE SampleDB;
GO
```

- use db

```sh
USE SampleDB;
GO
```

- create data

```sh
CREATE TABLE Products (
    ProductID INT PRIMARY KEY IDENTITY,
    ProductName NVARCHAR(100),
    Price DECIMAL(10, 2)
);
GO
```
