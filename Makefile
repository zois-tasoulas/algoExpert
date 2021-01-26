CC = g++
CPP_FLAGS = -Wall -Werror -Wextra -std=c++14 -pedantic -O3

SOURCEDIRS = easy medium
TARGETDIR = build

SOURCES = $(foreach dir,$(SOURCEDIRS),$(wildcard $(dir)/*.cpp))
TARGETS = $(foreach dir,$(SOURCEDIRS),$(patsubst $(dir)/%.cpp,$(TARGETDIR)/%,$(filter $(dir)/%,$(SOURCES))))

VPATH = $(SOURCEDIRS)

.PHONY: all
all: dir $(TARGETS)

dir:
	mkdir -p build

$(TARGETS) : $(TARGETDIR)/% : %.cpp Makefile
	$(CC) $(CPP_FLAGS) $< -o $@

.PHONY: clean
clean:
	@rm -rf build/
