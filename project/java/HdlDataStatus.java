package None;

import java.util.List;
import lombok.*;






/**
  The data class for the PID status information.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataStatus  {

  private String format;
  private String value;

}
