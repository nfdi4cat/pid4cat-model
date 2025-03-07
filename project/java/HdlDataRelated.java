package None;

import java.util.List;
import lombok.*;



/* version: 0.0.0 */


/**
  The data class for related identifiers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class HdlDataRelated  {

  private String format;
  private List<Pid4CatRelation> value;

}
