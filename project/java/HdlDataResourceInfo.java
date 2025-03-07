package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  The data class for the resource info.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataResourceInfo  {

  private String format;
  private ResourceInfo value;

}
