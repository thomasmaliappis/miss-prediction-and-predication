CC=gcc
CFLAGS=-Wformat=2 -Wformat-signedness -Wextra -Wall -Wpedantic -Werror -pedantic-errors -O3
BINARIES=\
	sort-branched \
	sort-predicated

%: %.c
	$(CC) $(CFLAGS) -o $@ $<

.PHONY: all clean

all: $(BINARIES)

clean:
	rm -v $(BINARIES)
