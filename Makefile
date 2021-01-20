.PHONY: all clean
CC = g++
CPP_FLAGS = -Wall -Werror -Wextra -std=c++14 -O3

SOURCEDIRS = easy medium
TARGETDIR = build

SOURCES = $(foreach dir,$(SOURCEDIRS),$(wildcard $(dir)/*.cpp))
TARGETS = $(foreach dir,$(SOURCEDIRS),$(patsubst $(dir)/%.cpp,$(TARGETDIR)/%.out,$(filter $(dir)/%,$(SOURCES))))

VPATH = $(SOURCEDIRS)

all: dir $(TARGETS) rename

dir:
	mkdir -p build

rename:
	for file in $(TARGETDIR)/*.out
	do
		mv "$file" "${file%%.out}"
	done

$(TARGETDIR)/%.out: %.cpp Makefile
	$(CC) $(CPP_FLAGS) $< -o $@

clean:
	@rm -rf build/
