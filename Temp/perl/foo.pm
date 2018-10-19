package foo;

##########################################################################
# Script start.
print $THIS_NAME, " package started\n";


# You can also import package variables,
# but the practice is strongly discouraged.

# use strict;
# use warnings;
use Exporter;

# Constants (Global).
use   constant    ARGMS_CRCT_GLBL     => 2;

# Globals.
my    $THIS_NAME = $0;

our @ISA= qw( Exporter );

# these CAN be exported.
our @EXPORT_OK = qw( export_me export_me_too );

# these are exported by default.
# our @EXPORT = qw( export_me  );
our @EXPORT = qw( checkReturnArguments get_two );

sub export_me {
    # stuff
}

sub export_me_too {
    # stuff
}

# sub checkReturnArguments()
sub checkReturnArguments
{
   # variables.
   my $cnt_argms; # total number of arguments passed.
   
   # get it.
   $cnt_argms = scalar(@_);
   
   # check it.
   #
   # If Incorrect.
   if ($cnt_argms != ARGMS_CRCT_GLBL)
   # If we used Readonly package (see above) then the following must be used:
   #    if ($cnt_argms != $ARGMS_CRCT_GLBL)
   #
   {
      # Then print message and exit.
      # print "\nError: Bad usage.\nMust be: ";
      print "0\n";
      # exit 9;
   }
   # Else same.
   else
   {
      # my $fst_arg = $_[0];
      # print "\nSame\n";
      # print "1\n";
      print $_[0], " ", $_[1], "\n";
      # return ("111", "222"); $_[0], " ", $_[1]
      return ($_[0], $_[1]);
   }
   
   # Else Correct.
   #
   # Assign variables.
   
   # print "Hello, World!\n";
}

sub get_two()
# sub get_two
{
   return ("one", "two");
}

# # Functions.
# sub checkArguments{
   # # variables.
   # my $cnt_argms; # total number of arguments passed.
   
   # # get it.
   # $cnt_argms = scalar(@_);
   
   # # check it.
   # #
   # # If Incorrect.
   # # if ($cnt_argms != $ARGMS_CRCT_GLBL)
   # # if ($cnt_argms != ARGMS_CRCT_GLBL)
   # if ($cnt_argms != 2)
   # {
      # # Then print message and exit.
      # print "\nError: Bad usage.\nMust be: ";
      # # exit 9;
   # }
   # else
   # {
      # print "\nSame\n";
   # }
   
   # # Else Correct.
   # #
   # # Assign variables.

##########################################################################
# Script end.   
print $THIS_NAME, " package ended\n";

# ?????
# 1;
