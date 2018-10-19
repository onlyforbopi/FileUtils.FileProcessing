package CheckReturnArguments_pm;

# Uses.
use Exporter;
#use strict;
#use warnings;
# use autodie;
# use Encode;
# use utf8;
use Text::Tabs;
# use Text::Unidecode;
# Text:Unidecode would also solve this problem but needs special installation
# Encode; is necessary for decode_utf8
# Alternate version : Use $ARGS[0,1...] so that user can supply input files as parameters (TO DO)
# use Readonly;

# Globals.
my    $THIS_NAME = $0 . " package 01";

# Script start.
print $THIS_NAME, " started\n";

# Constants (Global).
use   constant    THIS_NAME     => $0;
use   constant    ARGMS_CRCT_GLBL     => '2';
# Readonly    my    $ARGMS_CRCT_GLBL    => 2;

our @ISA= qw( Exporter );

# # these CAN be exported.
# our @EXPORT_OK = qw( export_me export_me_too );

# these are exported by default.
our @EXPORT = qw( chkRtrnArgs get_two );

# # Subroutines' prototypes.
# # ???*** WHY NOT WORKING ***???
# sub checkArguments();
sub chkRtrnArgs
{
   print "sub chkRtrnArgs started\n";
   
   # variables.
   my $cnt_argms; # total number of arguments passed.
   
   # get it.
   # $cnt_argms = scalar(@_);
   $cnt_argms = $_[0]; # Due to calling.
   
   print "cnt_argms       = $cnt_argms.\n";
   print "ARGMS_CRCT_GLBL = ", ARGMS_CRCT_GLBL, ".\n";
   
   # check it.
   #
   # If Incorrect.
   # THIS FAILS: if ($cnt_argms != ARGMS_CRCT_GLBL)
   if ($cnt_argms != ARGMS_CRCT_GLBL)
   # if ($cnt_argms ne $ARGMS_CRCT_GLBL)
   # If we used Readonly package (see above) then the following must be used:
   #    if ($cnt_argms != $ARGMS_CRCT_GLBL)
   {
      print "0\n";
      # Then print message and exit.
      print "\nError: Bad number of arguments: $cnt_argms. Must be: ", ARGMS_CRCT_GLBL, ".\n";
      print "Correct Usage: $0 <FileFilter> <FileBase>\n";
      print "@", $_[0], "@", $_[1], "@", $_[2], "@\n";
      print "Exiting with status: ", 9, ".\n";
      exit 9;
   }
   # Else same.
   else
   {
      print "1\n";
      # my $fst_arg = $_[0];
      # print "\nSame\n";
      # return ("111", "222"); $_[0], " ", $_[1]
      print "@", $_[0], "@", $_[1], "@", $_[2], "@\n";
      return ($_[1], $_[2]);
   }
   
   # Else Correct.
   #
   # Assign variables.
   
   # print "Hello, World!\n";
   # print "sub chkRtrnArgs ended\n";
} # chkRtrnArgs  ends.

# Script end.
print $THIS_NAME, " ended\n";

# Subroutines' body.

# # Subroutines' body.
# sub checkArguments_WRONG()
# {
   # # variables.
   # my $cnt_argms; # total number of arguments passed.
   
   # # get it.
   # $cnt_argms = scalar(@_);
   
   # # check it.
   # #
   # # If Incorrect.
   # if ($cnt_argms != ARGMS_CRCT_GLBL)
   # # If we used Readonly package (see above) then the following must be used:
   # #    if ($cnt_argms != $ARGMS_CRCT_GLBL)
   # #
   # {
      # # Then print message and exit.
      # # print "\nError: Bad usage.\nMust be: ";
      # print "0\n";
      # # exit 9;
   # }
   # # Else same.
   # else
   # {
      # # print "\nSame\n";
      # print "1\n";
   # }
   
   # # Else Correct.
   # #
   # # Assign variables.
   
   # # print "Hello, World!\n";
# }
