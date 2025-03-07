package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  The data class for the schema version.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataSchemaVer  {

  private String format;
  private String value;

}
