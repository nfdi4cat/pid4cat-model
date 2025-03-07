package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  The data class for the PID status information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataStatus  {

  private String format;
  private String value;

}
