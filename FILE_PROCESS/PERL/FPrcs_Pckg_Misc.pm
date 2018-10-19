package FPrcs_Pckg_Misc;

use strict;
use warnings;

use Readonly;
use Exporter;

# Globals.
our @ISA = qw( Exporter );
#
# Functions exported by default.
our @EXPORT = qw( chkRtrnArgs );

# Functions' Prototype. # "forward declaration".
sub chkRtrnArgs;

# Functions' Body.
sub chkRtrnArgs
{
   # Variables.
   my $cnt_argms = $_[0]; # Due to calling. # total   number of arguments passed.
   my $cor_argms = $_[1]; # Due to calling. # correct number of arguments passed.
   
   # Check them.
   #
   # If Incorrect.
   if ($cnt_argms != $cor_argms)
   {
      # Then print message and exit.
      print "\nError: Bad number of arguments:", $cnt_argms, ". Must be: ", $cor_argms, ".\n";
      exit 9;
   }
   # Else correct.
   else
   {
      return ($_[2], $_[3]); # Due to calling.
   }
} # chkRtrnArgs  ends.

1;
