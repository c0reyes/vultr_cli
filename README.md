# vultr_cli

cli for vultr API

In first proposal is created a simple way to perform virtual machine snapshot.

# Requirements

- Python 3.5

# Running vultr_cli

## Create API KEY

	./vultr_cli -c

## Help

	./vultr_cli -h

## Display Account

    ./vultr_cli account

## List Virtual Machine

	./vultr_cli server

## Snapshot

### List

    ./vultr_cli snapshot -l

### Create 

    ./vultr_cli snapshot -c SUBID -o Description

### Destroy

    ./vultr_cli snapshot -d SNAPSHOTID

