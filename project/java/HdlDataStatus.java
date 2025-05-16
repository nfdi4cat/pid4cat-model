package None;

import java.util.List;
import lombok.*;



/* version: 0.3.0.post26.dev0+e73dc8d */


/**
  The data class for the PID status information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataStatus  {

  private String format;
  private String value;

}
