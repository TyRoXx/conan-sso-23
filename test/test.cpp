#include <string.hpp>
#include <cassert>

int main()
{
	auto test_string = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
	std::size_t test_size = 62;

	auto i = test_size;
	do {
		auto const string_length = test_size - i;
		sso23::string str{test_string + i, string_length};
		assert(str.size() == string_length);

		auto const sso_capacity = sso23::string::sso_capacity;
		auto const capacity = std::max(sso_capacity, string_length);
		assert(str.capacity() == capacity);
		assert(str == test_string + i);
	} while(i-- != 0);
}
