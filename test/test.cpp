#include "lest.hpp"

#define CASE( name ) lest_CASE( specification, name )

static lest::tests specification;

CASE("Test lest conan package")
{
    EXPECT( "hello world" == "hello world" );
}

int main( int argc, char * argv[] )
{
    return lest::run( specification, argc, argv /*, std::cout */ );
}
