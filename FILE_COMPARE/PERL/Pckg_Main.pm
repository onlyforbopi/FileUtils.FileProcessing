package Pckg_Main;

use strict;
use warnings;

use Readonly;
use Exporter;

# FILES.
# FILES' NAMES.
# INPUT.
my $file_name_fltr;
my $file_name_base;
# OUTPUT: From file_name_base above.
my $file_name_xstY;
my $file_name_xstN;
# FILES' HANDLES.
# INPUT: Declare.
my $file_hndl_fltr;
my $file_hndl_base;
#
# OUTPUT: Declare.
my $file_hndl_xstY;
my $file_hndl_xstN;

# Globals.
# Constants.
Readonly my    $THIS_NAME => $0 . " package";
Readonly my    $NUM_ARGS  => $#ARGV + 1;
Readonly my    $COR_ARGS  => 2;
#
our @ISA= qw( Exporter );
# Exported Functions.
our @EXPORT = qw( fileCmpr ); # These are exported by default.
# our @EXPORT = qw( fileCmpr loadFltr2Table cmprBase2Fltr); # These are exported by default.
#
# our @EXPORT_OK = qw( loadFltr2Table cmprBase2Fltr); # These can be exported.
#
# Variables.
# Hashes.
our %fltr_hash;

# Functions' Prototype. # "forward declaration".
sub fileCmpr;

# Functions Body.
sub fileCmpr
{
   # Functions Prototype + Body.
   sub loadFltr2Table
   {
      my ($line, $load);
      
      # Load Filter to table.
      open $file_hndl_fltr, '<', $file_name_fltr;
      while ($line = <$file_hndl_fltr>) 
      {
         # Substring loaded into filter (Offset 0! - Always one less than n++)
         $load = substr("$line", 0, 11); # from,length.
         
         # Increment hash value for each string loaded
         $fltr_hash{$load}++
      }

      return (0);
   }
   # loadFltr2Table ends.

   sub cmprBase2Fltr
   {
      my ($line, $srch, $chek);
      
      # Read Base and check with Filter (table).
      open $file_hndl_base, '<', $file_name_base;
      while ($line = <$file_hndl_base>) 
      {
         
         $srch = substr("$line", 24, 11); # (Offset 0! - Always one less than length!)
         
         # check = search value.
         $chek = $fltr_hash{$srch};
         
         # If Base exists in Filter.
         if (exists $fltr_hash{$srch})
         {
            # Write input line to output file xstY.
            print {$file_hndl_xstY} "$line";
         }
         # Else Base doesn't exist in Filter.
         else
         {
            # Write input line to output file xstN.
            print {$file_hndl_xstN} "$line";
         }
      }

      return (0);
   }
   # cmprBase2Fltr ends.

   # FILES' NAMES.
   #
   # INPUT: From subroutine's Parameters.
   # ***!!! 
   # ***!!! ASSSUMING PROVIDED --> CHECKED in RUN Job. !!!***
   #        Could be checked like this:
   #        my ($file_name_fltr, $file_name_base) = chkRtrnArgs($NUM_ARGS, $ARGMS_CRCT_GLBL, $ARGV[0], $ARGV[1]);
   # ***!!! 
   $file_name_fltr = $_[0];
   $file_name_base = $_[1];
   #
   # OUTPUT: From file_name_base above.
   $file_name_xstY = $file_name_base . ".xstY";
   $file_name_xstN = $file_name_base . ".xstN";;
   
   print "FILE_OT_xstY: $file_name_xstY\n";
   print "FILE_OT_xstN: $file_name_xstN\n";
   
   # OUTPUT FILES: Open.
   open $file_hndl_xstY, '>', $file_name_xstY;
   open $file_hndl_xstN, '>', $file_name_xstN;
   
   loadFltr2Table();
   cmprBase2Fltr();
   
   return (0);
}
# fileCmpr  ends.

#
# ???!!! WHY 
#        is the following command needed,
#        !* ONLY *! for this package?
# ???!!! WHY
#
1;
